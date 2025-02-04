from persiantools import characters, digits

# pn = digits.en_to_fa("0987654321")
# pn = digits.fa_to_en("۰۹۸۷۶۵۴۳۲۱")
pn = digits.to_word(42226000)
print(pn, "تومان")
