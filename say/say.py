import re


small_numbers = dict(
    enumerate(
        [
            'zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen'
        ]
    )
)
tens = {
    20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
    60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
}



def say(number, recursive=False):
    number_sequence = [20, 100, 1e3, 1e6, 1e9, 1e12]

    if 0 <= number < 1e12:
        raise AttributeError('number is negative: ' + str(number))

    if number < 20:
        if recursive:
            return 'and ' + small_numbers[number]
        else:
            return small_numbers[number]

    if number < 100:
        if number % 10 == 0:
            return tens[number]
        return tens[(number // 10) * 10] + '-' + small_numbers[number % 10]

    if number < thousand:
        if number % 100 == 0:
            return small_numbers[number // 100] + ' hundred'
        return small_numbers[number // 100] + ' hundred and ' + say(number % 100, recursive=True)

    if number < million:
        if number % thousand == 0:
            return say(number // thousand) + ' thousand'
        return say(number // thousand) + ' thousand ' + say(number % thousand, recursive=True)

    if number < billion:
        if number % million == 0:
            return say(number // million) + ' million'
        return say(number // million) + ' million ' + say(number % million, recursive=True)

    if number < trillion:
        if number % billion == 0:
            return say(number // billion) + ' billion'
        return say(number // billion) + ' billion ' + say(number % billion, recursive=True)