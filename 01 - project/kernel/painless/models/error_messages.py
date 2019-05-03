class Messages :
    required = 'این فیلد اجباری است'
    email_validation = 'لطفا ایمیلتان را بدرستی وارد نمایید'

    def max_length (self, number):
        return ' لطفا تعداد کاراکتر بیش از {} باید باشد'.format(number)