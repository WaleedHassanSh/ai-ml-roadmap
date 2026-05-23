#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long card_number = get_long_long("Number: ");
    long long card_number_copy = card_number;

    int count = 0;

    while (card_number_copy > 0)
    {
        card_number_copy /= 10;
        count++;
    }

    card_number_copy = card_number;

    int sum1 = 0;
    int sum2 = 0;

    while (card_number_copy > 0)
    {
        sum2 += card_number_copy % 10;

        card_number_copy /= 10;

        if (card_number_copy == 0)
        {
            break;
        }

        int number = card_number_copy % 10;
        number *= 2;

        if (number > 9)
        {
            sum1 += number % 10;
            sum1 += number / 10;
        }

        else
        {
            sum1 += number;
        }

        card_number_copy /= 10;
    }

    int total = sum1 + sum2;

    card_number_copy = card_number;

    while (card_number_copy >= 100)
    {
        card_number_copy /= 10;
    }

    if (total % 10 != 0)
    {
        printf("INVALID\n");
    }

    else if (count == 15 && (card_number_copy == 34 || card_number_copy == 37))
    {
        printf("AMEX\n");
    }

    else if (count == 16 && (card_number_copy >= 51 && card_number_copy <= 55))
    {
        printf("MASTERCARD\n");
    }

    else if ((count == 13 || count == 16) && card_number_copy / 10 == 4)
    {
        printf("VISA\n");
    }

    else
    {
        printf("INVALID\n");
    }
}
