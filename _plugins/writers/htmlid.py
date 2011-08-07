import hashlib
from sphinx.writers.html import HTMLWriter, HTMLTranslator, \
     SmartyPantsHTMLTranslator


class HTMLIdTranslator(SmartyPantsHTMLTranslator):
    """An HTML translator that includes incremented ids and anchors"""
    id_counter = 0
    # def __init__(self, builder, *args, **kwargs):
    #     super(HTMLIdTranslator, self).__init__(builder, *args, **kwargs)
    #     self.id_counter = 0
    
    def visit_paragraph(self, node):
        self.id_counter += 1
        hashname = u"%s%s%s" % (self.builder.current_docname, self.id_counter, node.astext())
        id_name = hashlib.sha1(hashname.encode('utf8')).hexdigest()
        node['ids'].append(id_name)
        
        if self.should_be_compact_paragraph(node):
            self.context.append('')
        else:
            self.body.append('<a name="%s"></a>' % id_name)
            self.body.append(self.starttag(node, 'p', '', CLASS='cn'))
            self.context.append('</p>\n')
    
    def visit_block_quote(self, node):
        self.id_counter += 1
        node['ids'].append(str(self.id_counter))
        
        self.body.append(self.starttag(node, 'blockquote', CLASS='cn') + '<div>')
    
    ###
    # The li items usually have p tags in them. Don't need to have nested cn's
    
    # def visit_definition_list(self, node):
    #     self.id_counter += 1
    #     node['ids'].append(str(self.id_counter))
    #     
    #     self.body.append(self.starttag(node, 'dl', CLASS='docutils cn'))
    # 
    # def visit_list_item(self, node):
    #     self.id_counter += 1
    #     node['ids'].append(str(self.id_counter))
    #     
    #     self.body.append(self.starttag(node, 'li', '', CLASS='cn'))
    #     if len(node):
    #         node[0]['classes'].append('first')
    
    