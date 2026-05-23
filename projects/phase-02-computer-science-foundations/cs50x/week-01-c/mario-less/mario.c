#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    } while (height < 1);

    int spaces = height;

    for (int i = 0; i < height; i++)
    {
        print_row(spaces, i + 1);
        spaces--;
    }
}

void print_row(int spaces, int bricks)
{
    for (int j = spaces; j > 1; j--)
    {
        printf(" ");
    }

    for (int k = 0; k < bricks; k++)
    {
        printf("#");
    }

    printf("\n");
}
