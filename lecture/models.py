from django.db import models


class Lecture(models.Model):
    lectureidx = models.AutoField(db_column='lectureIdx', primary_key=True)  # Field name made lowercase.
    lecturename = models.CharField(db_column='lectureName', max_length=60)  # Field name made lowercase.
    price = models.CharField(max_length=20)
    lecturelink = models.TextField(db_column='lectureLink')  # Field name made lowercase.
    thumburl = models.TextField(db_column='thumbUrl', blank=True, null=True)  # Field name made lowercase.
    level = models.DecimalField(max_digits=4, decimal_places=3)
    lecturer = models.CharField(max_length=300, blank=True, null=True)
    siteidx = models.IntegerField(db_column='siteIdx')  # Field name made lowercase.
    rating = models.DecimalField(max_digits=4, decimal_places=3)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.CharField(db_column='isDeleted', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lecture'
