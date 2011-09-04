class EntryAdmin(admin.ModelAdmin):
    form = EntryForm
    
    list_display = ('title', 'pub_date', 'author')
    prepopulated_fields = { 'slug': ['title'] }
    readonly_fields = ('last_modified', 'last_modified_by',)
    fieldsets = ((
        None, {
            'fields': ('title', 'body', 'pub_date')
        }), (
        'Other Information', {
            'fields': ('last_modified', 'last_modified_by', 'slug'),
            'classes': ('collapse',)
        })
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.author.id:
            obj.author = request.user
        obj.last_modified_by = request.user
        obj.save()