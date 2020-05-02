from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    master_thesis_title = models.CharField(max_length=250)
    master_thesis_abstract = models.TextField(blank=True, null=True)
    instagram_handle = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    background = models.ImageField(upload_to='zimmern', blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        return "<Student: {} {}>".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("zimmer", kwargs={'slug': self.slug})


class Media(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    legend = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='artworks', blank=True, null=True)
    html_embed = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("medias")
        ordering = ["name"]

    def __str__(self):
        return "{} - {}".format(self.student, self.name)

    def __repr__(self):
        return "<Media: {} - {}>".format(self.student, self.name)

    def get_absolute_url(self):
        return reverse("media", kwargs={"pk": self.id})


class Orte(models.Model):
    name = models.CharField(max_length=100)
    background = models.ImageField(upload_to='orten', blank=True, null=True)
    previous = models.ForeignKey("Orte", on_delete=models.CASCADE, blank=True, null=True, related_name="previous_orte")
    next = models.ForeignKey("Orte", on_delete=models.CASCADE, blank=True, null=True, related_name="next_orte")
    entrance = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = _("orte")
        verbose_name_plural = _("orten")
        ordering = ["name"]

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "<Orte: {}>".format(self.name)

    def get_absolute_url(self):
        return reverse("orte", kwargs={'slug': self.slug})


class POI(models.Model):
    name = models.CharField(max_length=100)
    orte = models.ForeignKey(Orte, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    position_x = models.IntegerField(default=100)
    position_y = models.IntegerField(default=100)
    overlay = models.BooleanField(default=True)
    poi_image = models.ImageField(upload_to='poi', blank=True, null=True)

    class Meta:
        verbose_name = _("POI")
        verbose_name_plural = _("POI")
        ordering = ["orte", "name"]

    def __str__(self):
        return "{} - {}".format(self.orte, self.name)

    def __repr__(self):
        return "<POI: {} - {}>".format(self.orte, self.name)

    def get_absolute_url(self):
        return reverse("poi", kwargs={"pk": self.id})
