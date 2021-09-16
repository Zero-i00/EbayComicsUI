from django.db import models

GRADES = (
    ('0.5', '0.5'),
    ('1.0', '1.0'),
    ('1.5', '1.5'),
    ('1.8', '1.8'),
    ('2.0', '2.0'),
    ('2.5', '2.5'),
    ('3.0', '3.0'),
    ('3.5', '3.5'),
    ('4.0', '4.0'),
    ('4.5', '4.5'),
    ('5.0', '5.0'),
    ('5.5', '5.5'),
    ('6.0', '6.0'),
    ('6.5', '6.5'),
    ('7.0', '7.0'),
    ('7.5', '7.5'),
    ('8.0', '8.0'),
    ('8.5', '8.5'),
    ('9.0', '9.0'),
    ('9.2', '9.2'),
    ('9.4', '9.4'),
    ('9.6', '9.6'),
    ('9.8', '9.8'),
)


def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


# Create your models here.
class SnipeModel(models.Model):
    ebay_item_number = models.CharField(null=False, blank=False, max_length=255)
    gocollect_link = models.URLField(null=False, blank=False)
    max_percent_of_price = models.IntegerField(null=False)
    min_percent_of_price = models.IntegerField(null=True, blank=False, default=85)
    lowest_grade = models.CharField(default='0', choices=Reverse(GRADES), blank=False, null=False, max_length=255)
    highest_grade = models.CharField(default='10',choices=Reverse(GRADES), blank=False, null=False, max_length=255)
    negative_words = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return(self.pk)