// A program that computes the approximate grade level needed to comprehend some text, using the Coleman - Liau index.

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(int length, string text);
int count_words(int length, string text);
int count_sentences(int length, string text);

int main(void)
{
    string text = get_string("Text: ");

    int length = strlen(text);

    int letters = count_letters(length, text);
    int words = count_words(length, text);
    int sentences = count_sentences(length, text);

    float L = (letters / (float)words) * 100;
    float S = (sentences / (float)words) * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(int length, string text)
{
    int letters = 0;

    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }

    return letters;
}

int count_words(int length, string text)
{
    int words = 1;

    for (int i = 0; i < length; i++)
    {
        if (isspace(text[i]))
        {
            words++;
        }
    }

    return words;
}

int count_sentences(int length, string text)
{
    int sentences = 0;

    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }

    return sentences;
}
