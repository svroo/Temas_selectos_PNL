# Created by: Salazar Vega Rodrigo
import re


def email_valid(email):
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )

    if re.fullmatch(regex, email):
        return "Es un email\n"
    else:
        return "No es un email\n"


def valid_ip(ip: str):
    regex = re.compile(
        r"\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b"
    )

    if re.fullmatch(regex, ip):
        return "Es una ip\n"
    else:
        return "No es una ip\n"


def validDateHour(date):
    regex = re.compile(
        r"^(19[0-9]{2}|2[0-9]{3})-(0[1-9]|1[012])-([123]0|[012][1-9]|31) ([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
    )

    if re.fullmatch(regex, date):
        return "Es una fecha y hora\n"
    else:
        return "No es una fecha ni hora\n"


def validCurp(curp):
    regex = re.compile(
        r"[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}"
    )

    if re.fullmatch(regex, curp):
        return "Es un curp\n"
    else:
        return "No es un curp\n"


def validRfc(rfc):
    regex = re.compile(
        r"^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$"
    )

    if re.fullmatch(regex, rfc):
        return "Es un RFC\n"
    else:
        return "No es un RFC\n"


def boleta(boleta):
    regex = re.compile(r"\d{1,10}")
    if re.fullmatch(regex, boleta):
        return "Es una boleta\n"
    else:
        return "No es una boleta\n"


def validPhone(phone):
    regex = re.compile(
        r"^((\+52\s?)?(\s?9\s?)?\d{2,3}[\s-]?\d{3,4}-?\d{3,4}|\d{10,11}|(\d{3,4}[\s-]){1,2}\d{3,4})$"
    )

    if re.fullmatch(regex, phone):
        return "Es un telefono\n"
    else:
        return "No es un telefono\n"


def main(cadena):
    # print(
    #     f"La cadena ({cadena}) es:\
    #         \n{email_valid(cadena)}\n{valid_ip(cadena)}\n{validDateHour(cadena)}\n{validCurp(cadena)}\
    #             \n{validRfc(cadena)}\n{validPhone(cadena)}\n{boleta(cadena)}"
    # )
    print(
        "La cadena :",
        cadena,
        "es:\n" + email_valid(cadena),
        valid_ip(cadena),
        validDateHour(cadena),
        validCurp(cadena),
        validRfc(cadena),
        validPhone(cadena),
        boleta(cadena),
    )


if __name__ == "__main__":
    # email_valid("name.surname@gmail.com")
    main("2021630625")
