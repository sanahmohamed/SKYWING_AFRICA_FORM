from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('contact_number', models.CharField(max_length=50, verbose_name='Contact Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('nationality', models.CharField(max_length=100, verbose_name='Nationality')),
                ('budget', models.CharField(
                    choices=[('300K-1M', '300K - 1M'), ('1M-3M', '1M - 3M'), ('2.5M-5M', '2.5M - 5M')],
                    default='300K-1M', max_length=20, verbose_name='Budget')),
                ('property_type', models.CharField(
                    choices=[('TOWNHOUSE', 'Townhouse'), ('VILLA', 'Villa'), ('APPARTMENT', 'Appartment')],
                    default='TOWNHOUSE', max_length=20, verbose_name='Property Type')),
                ('date_of_attending', models.CharField(
                    choices=[('21-03-2026', '21-03-2026'), ('22-03-2026', '22-03-2026')],
                    default='21-03-2026', max_length=20, verbose_name='Date of Attending')),
                ('time_slot', models.CharField(
                    choices=[('9:00-12:00', '9:00 TO 12:00'), ('12:00-15:00', '12:00 TO 15:00'), ('15:00-18:00', '15:00 TO 18:00'), ('18:00-21:00', '18:00 TO 21:00')],
                    default='9:00-12:00', max_length=20, verbose_name='Time Slot')),
                ('reference', models.TextField(blank=True, null=True, verbose_name='Reference')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Registration',
                'verbose_name_plural': 'Registrations',
                'ordering': ['-submitted_at'],
            },
        ),
    ]
