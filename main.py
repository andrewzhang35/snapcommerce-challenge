"""
SnapCommerce data challenge
"""
import string
import pandas as pd

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> ' \
       '(12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;' \
       'Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'


def main():
    df = pd.DataFrame(i.split(";") for i in data.split("\n"))
    df = df.drop(6, axis=0)

    # Change flight codes
    codes = list(df[2][1:])
    prev_code = int(float(codes[0]))
    for i, code in enumerate(codes):
        if code == "":
            codes[i] = prev_code + 10
        else:
            codes[i] = int(float(code))

        prev_code = codes[i]

    df[2][1:] = codes

    # Split To_From into 2 columns
    to_from_list = list(df[3][1:])
    to_list = []
    from_list = []

    for to_from in to_from_list:
        split = to_from.split("_")
        to_list.append(split[0].upper())
        from_list.append(split[1].upper())

    df[3][0] = "To"
    df[3][1:] = to_list
    df.insert(4, 4, ["From", *from_list], True)

    # Clean airline codes
    airline_code_list = list(df[0][1:])

    for i, code in enumerate(airline_code_list):
        airline_code_list[i] = code.translate(str.maketrans("", "", string.punctuation)).strip()

    df[0][1:] = airline_code_list
    print(df)


if __name__ == "__main__":
    main()
