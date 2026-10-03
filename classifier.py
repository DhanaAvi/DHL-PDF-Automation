def classify_page(text):

    t = text.upper()

    if "WAYBILL DOC" in t:
        return "AWB"

    elif "COMMERCIAL INVOICE" in t:
        return "INV"

    elif "SHIPPING INVOICE" in t:
        return "INV"

    elif "رقم الفاتورة" in text:
        return "RFR"

    elif "قرار وزاري" in text:
        return "DEGREE"

    else:
        return "OTHER"