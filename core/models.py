from django.db import models

#from django.contrib.auth import get_user_model
#User = get_user_model()

from django.contrib.auth.models import User

class Slot(models.Model):
  doctor = models.ForeignKey(User, on_delete=models.CASCADE)
  is_reserved = models.BooleanField(default=False)
  date = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()

  def __str__(self):
        return self.doctor.username + " " + str(self.date) + " " + str(self.start_time) + " " + str(self.end_time)


class Appointment(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor.username + " " + self.patient.username + " " + str(self.slot.date) + " " + str(self.slot.start_time) + " " + str(self.slot.end_time)