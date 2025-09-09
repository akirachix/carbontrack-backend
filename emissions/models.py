from django.db import models
from django.db.models import Sum
from factory.models import MCU
from factory.models import Factory, EnergyEntry
from django.utils import timezone

class Emissions(models.Model):
    emissions_id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=255, null=True, blank=True)
    mcu = models.ForeignKey(MCU, on_delete=models.CASCADE, related_name='emissions' , null=True)
    emission_rate = models.DecimalField(max_digits=30, decimal_places=15)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" Emission {self.device_id} - {self.mcu.factory.factory_name}"
    
    @staticmethod
    def get_emission_sum_by_factory_and_date(factory_id, date):
        emissions = Emissions.objects.filter(
            mcu__factory_id=factory_id,
            updated_at__date=date
        ).aggregate(total_emission=Sum('emission_rate'))
        return emissions['total_emission'] or 0 

class Compliance(models.Model):
    compliance_id = models.AutoField(primary_key=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    compliance_target = models.DecimalField(max_digits=20, decimal_places=4, default=0)
    compliance_status = models.CharField(max_length=20, default='compliant', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_compliance_status(self, date=None):
        if date is None:
            date = timezone.now().date()
        tea_processed = EnergyEntry.get_tea_processed_sum_by_factory_and_date(self.factory.factory_id, date)
        co2_equivalent_sum = EnergyEntry.get_co2_sum_by_factory_and_date(self.factory.factory_id, date)
        emission_sum = Emissions.get_emission_sum_by_factory_and_date(self.factory.factory_id, date)
        total_emissions = co2_equivalent_sum + emission_sum
        
        co2_per_tea = total_emissions / tea_processed if tea_processed > 0 else 0
        
        if co2_per_tea > self.compliance_target or total_emissions > self.compliance_target:
            return 'non-compliant'
        else:
            return 'compliant'

    def save(self, *args, **kwargs):
        self.compliance_status = self.calculate_compliance_status()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Compliance for {self.factory.factory_name}"