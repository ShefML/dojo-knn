"""Script experiment with Iris dataset"""
import sys
import knn

def main():
    """Main entry point for the script."""
    knn.run_experiment(dataset_location = "../resources/phishing.data", features_count = 30)

if __name__ == '__main__':
    sys.exit(main())
