class Entry(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    pub_date = models.DateField(default=datetime.datetime.today)
    author = models.ForeignKey(
        User, 
        related_name='entries', 
        blank=True)
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        User, 
        related_name='entry_modifiers',
        blank=True)