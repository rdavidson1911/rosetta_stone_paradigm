import sys
from .main import main as parse_packets
from .forecasting_app import main as forecast
from .apt_dependency_visualizer import main as visualize_dependencies

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m rosetta_stone_paradigm [parse|forecast|visualize]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "parse":
        parse_packets()
    elif command == "forecast":
        forecast()
    elif command == "visualize":
        visualize_dependencies()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
