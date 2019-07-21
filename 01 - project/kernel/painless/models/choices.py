class PostStatus:
    """Check Published or Draft Status of a post
    
    Arguments:
        is_charfield {[bool]} -- check for charfield models or positiveintegerfield
    """

    def __init__(self, is_charfield = True):
               
        if is_charfield:
            self.DRAFT = 'd'
            self.PUBLISHED = 'p'
        else:
            self.DRAFT = 0
            self.PUBLISHED = 1
        
    
    def is_published(self, value):
        """[summary]
    
        Arguments:
            Postable {[str, int]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        return True if value == self.PUBLISHED else False
    
    def is_draft(self, value):
        return True if value == self.DRAFT else False
    
    def get_draft(self):
        return self.DRAFT
    
    def get_publish(self):
        return self.PUBLISHED
    
    def get_status(self):
        status = (
            (self.DRAFT, 'Draft'),
            (self.PUBLISHED, 'Published'),
        )

        return status





# #######
# colorstatus
#########
class SizeLevel:
    """Check Open or Close Status of a post
    
    Arguments:
        is_charfield {[bool]} -- check for charfield models or positiveintegerfield
    """

    def __init__(self, is_charfield = True):
               
        if is_charfield:
            self.SMALL = 's'
            self.XSMALL = 'xs'
            self.LARGE = 'l'
            self.XLARGE = 'xl'
            self.XXLARGE = 'xxl'
        else:
            self.SMALL = 0
            self.XSMALL = 1
            self.LARGE = 2
            self.XLARGE = 3
            self.XXLARGE = 4
    
    def is_small(self, value):
        """[summary]
    
        Arguments:
            Postable {[str, int]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        return True if value == self.SMALL else False
    
    def is_xsmall(self, value):
        return True if value == self.XSMALL else False

    def is_large(self, value):
        return True if value == self.LARGE else False

    def is_xlarge(self, value):
        return True if value == self.XLARGE else False

    def is_xxlarge(self, value):
        return True if value == self.XXLARGE else False



    def get_small(self):
        return self.SMALL
    
    def get_xsmall(self):
        return self.XSMALL
    
     
    def get_large(self):
        return self.LARGE


    def get_xlarge(self):
        return self.XLARGE

         
    def get_xxlarg(self):
        return self.XXLARGE


    def get_size(self):
        size = (
            (self.SMALL, 'Small'),
            (self.XSMALL, 'Xsmall'),
            (self.LARGE, 'Large'),
            (self.XLARGE, 'Xlarge'),
            (self.XXLARGE, 'Xxlarge'),
        )

        return size