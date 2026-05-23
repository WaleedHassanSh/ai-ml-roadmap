// A program that encrypts messages using a substitution cipher.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool only_alpha(string s);
bool only_unique(string s);
char substitute(char c, string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    else if (!only_alpha(argv[1]))
    {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }

    else if (!only_unique(argv[1]))
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }

    string key = argv[1];
    string plaintext = get_string("plaintext:  ");

    printf("ciphertext: ");

    for (int i = 0, length = strlen(plaintext); i < length; i++)
    {
        printf("%c", substitute(plaintext[i], key));
    }

    printf("\n");
}

bool only_alpha(string s)
{
    for (int i = 0, length = strlen(s); i < length; i++)
    {
        if (!isalpha(s[i]))
        {
            return false;
        }
    }

    return true;
}

bool only_unique(string s)
{
    for (int i = 0, length = strlen(s); i < length - 1; i++)
    {
        for (int j = i + 1; j < length; j++)
        {
            if (tolower(s[i]) == tolower(s[j]))
            {
                return false;
            }
        }
    }

    return true;
}

char substitute(char c, string key)
{
    if (isupper(c))
    {
        return toupper(key[c - 'A']);
    }

    else if (islower(c))
    {
        return tolower(key[c - 'a']);
    }

    else
    {
        return c;
    }
}
