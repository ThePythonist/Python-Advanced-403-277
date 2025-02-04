# import jdatetime
# import locale
#
# locale.setlocale(locale.LC_ALL, jdatetime.FA_LOCALE)
# now = jdatetime.datetime.now()
# weeekday = now.strftime("%A")
# print(weeekday)


from persiantools.jdatetime import JalaliDateTime

now = JalaliDateTime.now()
print(now.strftime("%A"))
