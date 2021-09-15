import argparse
import pathlib
import sys

from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-width", type=int)
    parser.add_argument("--max-height", type=int)
    parser.add_argument("images", nargs="*", type=pathlib.Path)

    args = parser.parse_args()

    err = []

    for image in args.images:
        if not image.exists():
            err.append(f"file {image} does not exist")
            continue
        i = Image.open(image)
        w, h = i.size

        if args.max_width:
            if w > args.max_width:
                err.append(f"image {image} is {w} pixels wide, maximum is {args.max_width}")

        if args.max_height:
            if h > args.max_height:
                err.append(f"image {image} is {h} pixels tall, maximum is {args.max_height}")

    if err:
        print("\n".join(err))
        sys.exit(1)


if __name__ == "__main__":
    main()
