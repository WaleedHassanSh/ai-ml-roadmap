// A program that recovers JPEGs from a forensic image of a memory card.

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "rb");

    if (card == NULL)
    {
        printf("Couldn't open file\n");
        return 1;
    }

    uint8_t buffer[512];
    int image_count = 0;
    FILE *output = NULL;

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output != NULL)
            {
                fclose(output);
            }

            char filename[8];
            sprintf(filename, "%03i.jpg", image_count);
            output = fopen(filename, "wb");

            if (output == NULL)
            {
                printf("Couldn't open file\n");
                fclose(card);
                return 1;
            }

            image_count++;
        }

        if (output != NULL)
        {
            fwrite(buffer, 1, 512, output);
        }
    }

    if (output != NULL)
    {
        fclose(output);
    }

    fclose(card);

    return 0;
}
