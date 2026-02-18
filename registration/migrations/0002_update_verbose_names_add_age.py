from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        # Remove Chinese verbose names, ensure age field exists
        migrations.AlterField(
            model_name='registration',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='contact_number',
            field=models.CharField(max_length=50, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='nationality',
            field=models.CharField(max_length=100, verbose_name='Nationality'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='budget',
            field=models.CharField(
                choices=[('300K-1M', '300K - 1M'), ('1M-3M', '1M - 3M'), ('2.5M-5M', '2.5M - 5M')],
                default='300K-1M',
                max_length=20,
                verbose_name='Budget'
            ),
        ),
        migrations.AlterField(
            model_name='registration',
            name='property_type',
            field=models.CharField(
                choices=[('TOWNHOUSE', 'Townhouse'), ('VILLA', 'Villa'), ('APPARTMENT', 'Appartment')],
                default='TOWNHOUSE',
                max_length=20,
                verbose_name='Property Type'
            ),
        ),
        migrations.AlterField(
            model_name='registration',
            name='date_of_attending',
            field=models.CharField(
                choices=[('21-03-2026', '21-03-2026'), ('22-03-2026', '22-03-2026')],
                default='21-03-2026',
                max_length=20,
                verbose_name='Date of Attending'
            ),
        ),
        migrations.AlterField(
            model_name='registration',
            name='time_slot',
            field=models.CharField(
                choices=[('9:00-12:00', '9:00 TO 12:00'), ('12:00-15:00', '12:00 TO 15:00'), ('15:00-18:00', '15:00 TO 18:00'), ('18:00-21:00', '18:00 TO 21:00')],
                default='9:00-12:00',
                max_length=20,
                verbose_name='Time Slot'
            ),
        ),
        migrations.AlterField(
            model_name='registration',
            name='reference',
            field=models.TextField(blank=True, null=True, verbose_name='Reference'),
        ),
    ]
