// A program that implements image filters for BMP files

#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red_sum = 0;
            int green_sum = 0;
            int blue_sum = 0;

            float total = 0;

            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if (k >= 0 && k < height && l >= 0 && l < width)
                    {
                        red_sum += copy[k][l].rgbtRed;
                        green_sum += copy[k][l].rgbtGreen;
                        blue_sum += copy[k][l].rgbtBlue;

                        total++;
                    }
                }
            }

            image[i][j].rgbtRed = round(red_sum / total);
            image[i][j].rgbtGreen = round(green_sum / total);
            image[i][j].rgbtBlue = round(blue_sum / total);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
            int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

            float Gx_red = 0;
            float Gy_red = 0;
            float Gx_green = 0;
            float Gy_green = 0;
            float Gx_blue = 0;
            float Gy_blue = 0;

            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if (k >= 0 && k < height && l >= 0 && l < width)
                    {
                        Gx_red += Gx[k - i + 1][l - j + 1] * copy[k][l].rgbtRed;
                        Gy_red += Gy[k - i + 1][l - j + 1] * copy[k][l].rgbtRed;
                        Gx_green += Gx[k - i + 1][l - j + 1] * copy[k][l].rgbtGreen;
                        Gy_green += Gy[k - i + 1][l - j + 1] * copy[k][l].rgbtGreen;
                        Gx_blue += Gx[k - i + 1][l - j + 1] * copy[k][l].rgbtBlue;
                        Gy_blue += Gy[k - i + 1][l - j + 1] * copy[k][l].rgbtBlue;
                    }
                }
            }

            int G_red = round(sqrt((Gx_red * Gx_red) + (Gy_red * Gy_red)));
            int G_green = round(sqrt((Gx_green * Gx_green) + (Gy_green * Gy_green)));
            int G_blue = round(sqrt((Gx_blue * Gx_blue) + (Gy_blue * Gy_blue)));

            if (G_red > 255)
            {
                G_red = 255;
            }

            if (G_green > 255)
            {
                G_green = 255;
            }

            if (G_blue > 255)
            {
                G_blue = 255;
            }

            image[i][j].rgbtRed = G_red;
            image[i][j].rgbtGreen = G_green;
            image[i][j].rgbtBlue = G_blue;
        }
    }
    return;
}
