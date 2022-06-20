
from ImageDistanceCataloger import ImageDistanceCataloger
import argparse
import sys
import click

def main():
    parser = argparse.ArgumentParser(description='add, modify and delete upstream nodes')
    parser.add_argument(
        '-r', '--radius', required=False, type=int, help='radius length in meters', default=1000
        )

    parser.add_argument(
        '-I', '--input', required=False, type=str, help='input directory path', default="./input"
        )
    parser.add_argument(
        '-O', '--output', required=False, type=str, help='output directory path', default="./output"
        )
    parser.add_argument(
        '-f', '--force', required=False,action='store_true', help='force overwrite output directory'
        )

    args = parser.parse_args()
    print("# Radius: {} meters, Input: {}, Output: {}".format(args.radius, args.input, args.output))
    print(args.force)
    try:
        cataloger = ImageDistanceCataloger(input=args.input, output=args.output, force=args.force)
        cataloger.group_by_distance(args.radius)
    except Exception as error:
        click.secho("# {0}".format(error), fg="red")
        sys.exit(1)


if __name__ == "__main__":
    main()