from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.subject} — {self.name}'


class SiteProfile(models.Model):
    """Site-wide content that the site owner manages from the admin panel."""

    profile_picture = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True,
        help_text='Square photo recommended (min 400x400). Shown in the hero section.',
    )
    resume_file = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True,
        help_text='Upload your resume as a PDF.',
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Profile'
        verbose_name_plural = 'Site Profile'

    def __str__(self):
        return 'Site Profile'

    def save(self, *args, **kwargs):
        if not self.pk and SiteProfile.objects.exists():
            existing = SiteProfile.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)
