import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path, encoding='utf-8-sig')

    # Data Cleaning
    df["Item Fat Content"] = df["Item Fat Content"].replace({
        "LF": "Low Fat",
        "reg": "Regular",
        "low fat": "Low Fat"
    })

    # Handle missing Item Weight values by filling with the mean
    df['Item Weight'] = df['Item Weight'].fillna(df['Item Weight'].mean())

    return df

def get_kpis(df):
    total_sale = df["Sales"].sum()
    avg_sale = df["Sales"].mean()
    item_count = df["Sales"].count()
    avg_ratings = df["Rating"].mean()

    return {
        "total_sales": round(total_sale, 2),
        "average_sales": round(avg_sale, 2),
        "number_of_items_sold": int(item_count),
        "average_rating": round(avg_ratings, 2)
    }

def get_plot_as_base64(plt):
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    return graphic.decode('utf-8')

def plot_sales_by_fat_content(df):
    sales_by_fat = df.groupby(["Item Fat Content"], as_index=False)["Sales"].sum()

    plt.figure(figsize=(6, 4))
    plt.pie(
        sales_by_fat["Sales"],
        labels=sales_by_fat["Item Fat Content"],
        autopct="%.1f%%",
        startangle=120,
        shadow=True
    )
    plt.title("Sales by Fat Content", fontsize=15)
    plt.axis("equal")
    plt.legend(title="Fat Content", fontsize=8, title_fontsize=9, fancybox=True)
    plt.tight_layout()
    graphic = get_plot_as_base64(plt)
    plt.close()
    return graphic

def plot_sales_by_item_type(df):
    sales_by_item_type = df.groupby(["Item Type"], as_index=False)["Sales"].sum().sort_values(by="Sales", ascending=False)

    plt.figure(figsize=(14, 8))
    sns.barplot(data=sales_by_item_type, x="Item Type", y="Sales", hue="Item Type", palette="viridis", legend=False)

    for index, value in enumerate(sales_by_item_type["Sales"]):
        plt.text(index, value + 1000, str(int(value)), ha="center", fontsize=13)

    plt.xticks(rotation=45, ha='right')
    plt.title("Sales by Item Types", fontsize=30)
    plt.xlabel("Item Type", fontsize=15)
    plt.ylabel("Total Sales", fontsize=15)
    plt.tight_layout()
    graphic = get_plot_as_base64(plt)
    plt.close()
    return graphic

def plot_fat_content_by_outlet_sales(df):
    sales_by_outlet_fat = df.groupby(["Outlet Location Type", "Item Fat Content"], as_index=False)["Sales"].sum()

    plt.figure(figsize=(14, 8))
    sns.barplot(data=sales_by_outlet_fat, x="Outlet Location Type", y="Sales", hue="Item Fat Content", palette="GnBu")

    plt.title("Fat Content by Outlet for Total Sales", fontsize=15)
    plt.xlabel("Outlet Location Type")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45, ha='right')
    plt.legend(title="Item Fat Content", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    graphic = get_plot_as_base64(plt)
    plt.close()
    return graphic

def plot_sales_by_outlet_establishment_year(df):
    total_sales_by_outlet_establishment = df.groupby(["Outlet Establishment Year"], as_index=False)["Sales"].sum()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=total_sales_by_outlet_establishment, x="Outlet Establishment Year", y="Sales", marker='o', color='green')

    x = total_sales_by_outlet_establishment["Outlet Establishment Year"]
    y = total_sales_by_outlet_establishment["Sales"]

    for i in range(len(x)):
        plt.text(x[i], y[i] + 6, str(int(y[i])), ha="center", fontsize=13)

    plt.title("Total Sales by Outlet Establishment Year", fontsize=15)
    plt.xlabel("Outlet Establishment Year")
    plt.ylabel("Total Sales")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    graphic = get_plot_as_base64(plt)
    plt.close()
    return graphic

def plot_sales_by_outlet_size(df):
    sales_by_outlet_size = df.groupby(["Outlet Size"], as_index=False)["Sales"].sum()

    plt.figure(figsize=(6, 4))
    plt.pie(
        sales_by_outlet_size["Sales"],
        labels=sales_by_outlet_size["Outlet Size"],
        autopct="%.1f%%",
        startangle=120,
        shadow=True
    )
    plt.title("Sales by Outlet Size", fontsize=15)
    plt.axis("equal")
    plt.legend(title="Outlet Size", fontsize=8, title_fontsize=9, fancybox=True)
    plt.tight_layout()
    graphic = get_plot_as_base64(plt)
    plt.close()
    return graphic

def plot_sales_by_outlet_location(df):
    sales_by_oulet_location = df.groupby(["Outlet Location Type"], as_index=False)["Sales"].sum().sort_values(by="Sales", ascending=False)

    plt.figure(figsize=(14, 8))
    sns.barplot(data=sales_by_oulet_location, x="Outlet Location Type", y="Sales", hue="Outlet Location Type", palette="viridis", legend=False)

    for index, value in enumerate(sales_by_oulet_location["Sales"]):
        plt.text(index, value + 10000, str(int(value)), va="center", fontsize=13)

    plt.title("Sales by Outlet Location", fontsize=30)
    plt.xlabel("Outlet Location Type", fontsize=15)
    plt.ylabel("Total Sales", fontsize=15)
    plt.tight_layout()
    graphic = get_plot_as_base64(plt)
    plt.close()
    return graphic