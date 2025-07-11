# Iris Dataset Visualization - Save Plots as PNG Images

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Display first few rows
print("First 5 rows of the dataset:")
print(iris.head())

# 1. Count of Each Species
plt.figure(figsize=(6, 4))
sns.countplot(data=iris, x='species', hue='species', palette='Set2', legend=False)
plt.title('Count of Each Iris Species')
plt.xlabel("Species")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plot1_species_count.png")
plt.close()

# 2. Pairplot – Relationship Between All Features
pairplot = sns.pairplot(iris, hue='species', palette='husl')
pairplot.fig.suptitle('Pairwise Relationships Between Features', y=1.02)
pairplot.savefig("plot2_pairplot.png")
plt.close()

# 3. Boxplot of Petal Length by Species
plt.figure(figsize=(6, 4))
sns.boxplot(data=iris, x='species', y='petal_length', palette='Pastel1')
plt.title('Petal Length by Species')
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig("plot3_boxplot_petal_length.png")
plt.close()

# 4. Scatter Plot: Petal Length vs Petal Width
plt.figure(figsize=(6, 4))
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', style='species', palette='Dark2')
plt.title('Petal Length vs Petal Width')
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.tight_layout()
plt.savefig("plot4_scatter_petal.png")
plt.close()

# 5. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(iris.drop('species', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig("plot5_correlation_heatmap.png")
plt.close()
