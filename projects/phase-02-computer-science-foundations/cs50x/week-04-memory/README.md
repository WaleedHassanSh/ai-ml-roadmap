# CS50x Week 04 — Memory

This folder contains my solutions for **CS50x Week 04: Memory** as part of my **AI/ML Roadmap — Phase 02: Computer Science Foundations**.

The goal of this week is to strengthen low-level C programming skills related to memory, file I/O, binary data, image processing, audio processing, pointers, arrays, and data recovery. These concepts are important because they build a stronger understanding of how data is represented, read, written, and manipulated at the byte level.

## Local Path

```bash
~/ai-ml-roadmap/projects/phase-02-computer-science-foundations/cs50x/week-04-memory/
```

## Topics Covered

- Memory and byte-level data representation
- File I/O in C
- WAV audio file processing
- BMP image processing
- JPEG file recovery
- `fopen`, `fread`, `fwrite`, and `fclose`
- Command-line arguments
- 8-bit and 16-bit integer types
- Structs
- 2D arrays
- Image filters
- Box blur
- Sobel edge detection
- Buffer-based file reading
- Detecting file signatures

## Problems Completed

| Problem | File / Folder | Status |
|---|---|---|
| Volume | `volume/volume.c` | Completed |
| Filter Less | `filter-less/helpers.c` | Completed |
| Filter More | `filter-more/helpers.c` | Completed |
| Recover | `recover/recover.c` | Completed |

## Folder Structure

```text
week-04-memory/
├── README.md
│
├── volume/
│   └── volume.c
│
├── filter-less/
│   ├── bmp.h
│   ├── filter.c
│   ├── helpers.c
│   ├── helpers.h
│   ├── Makefile
│   └── images/
│
├── filter-more/
│   ├── bmp.h
│   ├── filter.c
│   ├── helpers.c
│   ├── helpers.h
│   ├── Makefile
│   └── images/
│
└── recover/
    ├── recover.c
    └── card.raw
```

## Setup Commands

Run these commands from the root of the local repository:

```bash
cd ~/ai-ml-roadmap

mkdir -p projects/phase-02-computer-science-foundations/cs50x/week-04-memory

cd projects/phase-02-computer-science-foundations/cs50x/week-04-memory
```

Download the CS50x Week 4 distribution code:

```bash
wget https://cdn.cs50.net/2026/x/psets/4/volume.zip
unzip volume.zip
rm volume.zip

wget https://cdn.cs50.net/2026/x/psets/4/filter-less.zip
unzip filter-less.zip
rm filter-less.zip

wget https://cdn.cs50.net/2026/x/psets/4/filter-more.zip
unzip filter-more.zip
rm filter-more.zip

wget https://cdn.cs50.net/2026/x/psets/4/recover.zip
unzip recover.zip
rm recover.zip
```

## Problem Summaries

### 1. Volume

**File:** `volume/volume.c`

This program modifies the volume of a WAV audio file by multiplying each 16-bit audio sample by a given factor.

**Main concepts practiced:**

- Reading and writing binary files
- Copying a WAV header
- Processing audio samples
- Using `uint8_t` and `int16_t`
- Command-line arguments
- `fread()` and `fwrite()`

**Key idea:**

A WAV file starts with a 44-byte header. After copying the header unchanged, the program reads each 16-bit sample, multiplies it by the volume factor, and writes the modified sample to the output file.

Example:

```c
while (fread(&buffer, sizeof(int16_t), 1, input))
{
    buffer *= factor;
    fwrite(&buffer, sizeof(int16_t), 1, output);
}
```

---

### 2. Filter Less

**File:** `filter-less/helpers.c`

This program implements basic image filters for BMP files.

**Filters implemented:**

- Grayscale
- Sepia
- Reflection
- Blur

**Main concepts practiced:**

- 2D arrays
- Structs
- RGB pixel manipulation
- Nested loops
- Rounding with `round()`
- Swapping values
- Box blur using neighboring pixels

**Key idea:**

Each image is represented as a 2D array of `RGBTRIPLE` values. Each pixel has red, green, and blue components. The filters modify these pixel values directly.

---

### 3. Filter More

**File:** `filter-more/helpers.c`

This program extends image filtering by adding edge detection using the Sobel operator.

**Filters implemented:**

- Grayscale
- Reflection
- Blur
- Edges

**Main concepts practiced:**

- Sobel edge detection
- Convolution kernels
- Boundary checking
- Copying image data before modifying it
- Square root calculation with `sqrt()`
- Capping RGB values at 255

**Key idea:**

The edge detection filter calculates horizontal and vertical color changes using `Gx` and `Gy` kernels. The final pixel value is calculated using:

```text
sqrt(Gx^2 + Gy^2)
```

The result is rounded and capped at 255.

---

### 4. Recover

**File:** `recover/recover.c`

This program recovers JPEG files from a raw memory card image.

**Main concepts practiced:**

- Reading raw binary data
- Buffer-based file processing
- JPEG signature detection
- Creating output files dynamically
- Sequential file naming
- File recovery logic

**Key idea:**

JPEG files begin with a recognizable byte signature:

```text
ff d8 ff e0
ff d8 ff e1
...
ff d8 ff ef
```

The program reads the memory card in 512-byte blocks. Whenever it finds a JPEG signature, it starts writing a new JPEG file named `000.jpg`, `001.jpg`, `002.jpg`, and so on.

## Compile Commands

Run each command inside the relevant problem folder.

### Volume

```bash
cd volume
make volume
```

### Filter Less

```bash
cd filter-less
make filter
```

### Filter More

```bash
cd filter-more
make filter
```

### Recover

```bash
cd recover
make recover
```

## Test Commands

### Volume

```bash
./volume input.wav output.wav 2.0
./volume input.wav output.wav 0.5
```

### Filter Less

```bash
./filter -g images/yard.bmp out.bmp
./filter -s images/yard.bmp out.bmp
./filter -r images/yard.bmp out.bmp
./filter -b images/yard.bmp out.bmp
```

### Filter More

```bash
./filter -g images/yard.bmp out.bmp
./filter -r images/yard.bmp out.bmp
./filter -b images/yard.bmp out.bmp
./filter -e images/yard.bmp out.bmp
```

### Recover

```bash
./recover card.raw
```

## Check Commands

Run these commands from inside each problem folder.

```bash
check50 cs50/problems/2026/x/volume
check50 cs50/problems/2026/x/filter/less
check50 cs50/problems/2026/x/filter/more
check50 cs50/problems/2026/x/recover
```

## Style Commands

```bash
style50 volume.c
style50 helpers.c
style50 helpers.c
style50 recover.c
```

Recommended usage by folder:

```bash
cd volume
style50 volume.c

cd ../filter-less
style50 helpers.c

cd ../filter-more
style50 helpers.c

cd ../recover
style50 recover.c
```

## Submit Commands

Run these commands from inside each problem folder.

```bash
submit50 cs50/problems/2026/x/volume
submit50 cs50/problems/2026/x/filter/less
submit50 cs50/problems/2026/x/filter/more
submit50 cs50/problems/2026/x/recover
```

## Important Revision Notes

- A file is just a sequence of bytes.
- Headers store metadata about the file.
- WAV samples in this problem are 16-bit signed integers.
- BMP pixels are stored as `RGBTRIPLE` structs.
- BMP color values range from 0 to 255.
- For blur and edges, always read from a copy of the original image.
- For recover, read 512 bytes at a time because JPEG signatures are block-aligned.
- Always close files opened with `fopen()`.
- Check command-line arguments before using `argv`.
- Check whether `fopen()` returns `NULL`.

## Git Commands

From the repository root:

```bash
git add projects/phase-02-computer-science-foundations/cs50x/week-04-memory

git commit -m "Add CS50x Week 4 memory solutions"

git push
```
