# my_tts_project/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_metrics(process_times, real_time_factors, output_dir="viz_output"):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Plot processing times
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(range(1, len(process_times) + 1)), y=process_times)
    plt.xlabel('Phrase Index')
    plt.ylabel('Processing Time (seconds)')
    plt.title('Processing Time for Each Phrase')
    plt.savefig(os.path.join(output_dir, "processing_times.png"))
    plt.close()  # Close the figure to avoid display issues

    # Plot real-time factors
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(range(1, len(real_time_factors) + 1)), y=real_time_factors)
    plt.xlabel('Phrase Index')
    plt.ylabel('Real-Time Factor')
    plt.title('Real-Time Factor for Each Phrase')
    plt.savefig(os.path.join(output_dir, "real_time_factors.png"))
    plt.close()  # Close the figure to avoid display issues
