import argparse
from scripts.agents.drafter import DrafterAgent
from scripts.utils import load_json

def main(outline_path, out_path):
    outline_data = load_json(outline_path)

    agent = DrafterAgent()
    draft = agent.run(outline_data, out_path)
    print(f"Draft saved to: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--outline", default="data/outline.json", help="Outline JSON path")
    parser.add_argument("--out", default="data/draft.md", help="Output path")
    args = parser.parse_args()
    main(args.outline, args.out)
