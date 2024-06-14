import argparse
from utils import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, choices=['cifar', 'adult'], required=True, help="Dataset: 'cifar' or 'adult'")
    args = parser.parse_args()

    seed = 42
    set_seed(seed)  

    optimizers = ['sgd', 'adam', 'signsgd', 'adagrad', 'lion']
    complexities = [False, True]

    results = {}
    losses = {}

    for opti in optimizers:
        for complex in complexities:
            key = (opti, 'complex' if complex else 'simple')
            print(f"Testing combination: Optimizer={opti}, Model={'Complex' if complex else 'Simple'}")

            loss, final_accuracy, convergence_iter = run_experiment(optimizer_name=opti, use_complex_model=complex, dataset=args.dataset)
            results[key] = (final_accuracy, convergence_iter)
            losses[key] = loss

    if args.dataset == 'adult':
        print_results_table(results, "Adult")
        plot_loss_separate(losses, store=True, show=True, directory='plots/adult')
        plot_loss(losses, store=True, show=True, directory='plots/adult', filename='loss_plot_combined.png')
    elif args.dataset == 'cifar':
        print_results_table(results, "CIFAR-10")
        plot_loss_moving_average(losses, store=True, show=True, directory='plots/cifar', filename='loss_plot_cifar.png', window_size=1000)


if __name__ == '__main__':
    main()