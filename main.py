from repository import get_data


def main():
    data = get_data()
    results = compute(data)

if __name__ == '__main__':
    main()
