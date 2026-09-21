from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, help_text="e.g., Programming, Frontend, Backend, Database")
    proficiency = models.IntegerField(default=0, help_text="Percentage 0-100")
    icon = models.CharField(max_length=50, blank=True, help_text="Emoji or icon class")
    image = models.ImageField(upload_to='skills/', blank=True, null=True, help_text="Skill icon image (replaces icon)")

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    features = models.TextField(help_text="One feature per line")
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated technologies")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    demo_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-featured', 'title']

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]

class Education(models.Model):
    institution = models.CharField(max_length=300)
    degree = models.CharField(max_length=200)
    period = models.CharField(max_length=100, help_text="e.g., 2022 - 2026")
    cgpa = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', 'institution']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=300)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    period = models.CharField(max_length=100)
    description = models.TextField()
    achievements = models.TextField(blank=True, help_text="One achievement per line")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', 'company']

    def __str__(self):
        return f"{self.role} at {self.company}"
