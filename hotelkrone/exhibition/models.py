from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bachelor_thesis_title = models.CharField(max_length=250)
    bachelor_thesis_abstract = models.TextField(blank=True, null=True)
    portfolio = models.FileField(upload_to='portfolios', blank=True, null=True)
    instagram_handle = models.CharField(max_length=100, blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)
    project_website = models.URLField(blank=True, null=True)
    project_website2 = models.URLField(blank=True, null=True)
    kleio_profile = models.URLField(blank=True, null=True)
    background = models.ImageField(upload_to='zimmern', blank=True, null=True)
    hover_image = models.ImageField(upload_to='zimmern', blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    last_update = models.DateTimeField(auto_now=True)
    orten = models.ManyToManyField("Orte")

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
    sound = models.FileField(upload_to='artworks', blank=True, null=True)
    html_embed = models.TextField(blank=True, null=True)
    display_in_zimmer = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("media")
        verbose_name_plural = _("medias")
        ordering = ["order", "name"]

    def __str__(self):
        return "{} - {}".format(self.student, self.name)

    def __repr__(self):
        return "<Media: {} - {}>".format(self.student, self.name)

    def get_absolute_url(self):
        return reverse("media", kwargs={"pk": self.id})


class Orte(models.Model):
    EQUIRECTANGULAR = "EQUI"
    INFINITE = "INFI"
    NOJS = "NOJS"
    ANIMATE = [
      (EQUIRECTANGULAR, _('Equirectangular Picture')),
      (INFINITE, _('Infinite Scroll Picture')),
      (NOJS, _('Static Picture / Live Stream')),
    ]
    animation = models.CharField(max_length=4, choices=ANIMATE, default=EQUIRECTANGULAR)
    name = models.CharField(max_length=100)
    hover_image = models.ImageField(upload_to='orten', blank=True, null=True)
    background = models.ImageField(upload_to='orten', blank=True, null=True)
    background_sound = models.FileField(upload_to='sounds', blank=True, null=True)
    html_embed = models.TextField(blank=True, null=True)
    js_config = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    previous = models.ForeignKey("Orte", on_delete=models.CASCADE, blank=True, null=True, related_name="previous_orte")
    next = models.ForeignKey("Orte", on_delete=models.CASCADE, blank=True, null=True, related_name="next_orte")
    entrance = models.BooleanField(default=False)
    hide_on_entrance = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)
    order = models.IntegerField(default = 0)
    map_height = models.IntegerField(blank=True, null=True)
    map_width = models.IntegerField(blank=True, null=True)
    position_x = models.IntegerField(blank=True, null=True)
    position_y = models.IntegerField(blank=True, null=True)
    position_z = models.IntegerField(blank=True, null=True)
    zoom = models.FloatField(default=1)


    class Meta:
        verbose_name = _("orte")
        verbose_name_plural = _("orten")
        ordering = ["order", "name"]

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "<Orte: {}>".format(self.name)

    def get_absolute_url(self):
        if not self.entrance:
            return reverse("orte", kwargs={'slug': self.slug})
        else:
            return reverse("home")


class POI(models.Model):
    name = models.CharField(max_length=100)
    orte = models.ForeignKey(Orte, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    scale = models.IntegerField(default=100)
    css_class = models.CharField(max_length=150, blank=True, null=True)
    position_x = models.IntegerField(default=100)
    position_y = models.IntegerField(default=100)
    position_z = models.IntegerField(default=100)
    position_w = models.IntegerField(default=100)
    position_h = models.IntegerField(default=100)
    this_is_a_cat = models.BooleanField(default=False)
    poi_image = models.ImageField(upload_to='poi', blank=True, null=True)
    this_is_a_sound = models.BooleanField(default=False)
    hide_overlay = models.BooleanField(default=False)
    url_link = models.CharField(max_length=100, blank=True, null=True)
    this_specific_class_endless = models.BooleanField(default=False)
    this_fullscreen_video = models.BooleanField(default=False)

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


class TrackedFile(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to='files', blank=True, null=True)
    counter = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("tracked file")
        verbose_name_plural = _("tracked files")
        ordering = ["name"]

    def __str__(self):
        return "{} - {}".format(self.student, self.name)

    def __repr__(self):
        return "<Media: {} - {}>".format(self.student, self.name)

    def get_absolute_url(self):
        return reverse("file", kwargs={"pk": self.id})


class ContentManagement(models.Model):
    program = models.TextField(blank=True, null=True)
    display_program = models.BooleanField(default=True)
    impressum = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("content management")
        verbose_name_plural = _("contents management")
