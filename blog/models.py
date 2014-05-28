import datetime
import BeautifulSoup
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=240, blank=False, unique=True)
    slug = models.CharField(db_index=True, unique=True, max_length=50)
    entry = RichTextField()
    pub_date = models.DateField(default=datetime.datetime.now)
    publish = models.BooleanField(default=False,
                                  choices=[(True, "Yes"),
                                           (False, "No")],
                                  )

    def getPlainText(self):
        soup = BeautifulSoup.BeautifulSoup(self.entry)
        return " ".join(soup.findAll(text=True))

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    def getUrl(self):
        return reverse("post", args=[self.slug])
