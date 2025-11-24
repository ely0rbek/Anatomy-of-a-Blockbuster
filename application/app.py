from contextlib import contextmanager
import streamlit as st
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blockbuster_analysis.revenue_by_year import plot_revenue_by_year
from blockbuster_analysis.budget_vs_revenue import plot_budget_vs_revenue
from blockbuster_analysis.genre_avg_rating import plot_genre_avg_rating
from blockbuster_analysis.genre_avg_revenue import plot_genre_avg_revenue
from blockbuster_analysis.runtime_vs_revenue import plot_runtime_vs_revnue

@contextmanager
def get_plot_figure(plot_func, title):
    try:
        st.subheader(title)
        plot_func()
        fig = plt.gcf()
        yield fig
    except Exception as e:
        st.error(f"'{title}' grafigini chizishda kutilmagan xatolik yuz berdi:")
        st.exception(e)
        yield None
    finally:
        if 'fig' in locals() and fig is not None:
            plt.close(fig)

def main():
    st.set_page_config(page_title="Blockbuster Data Dashboard", layout="wide")
    st.title("Blockbuster Movies Data Analysis Dashboard")

    st.markdown("---")
    st.header("Vizualizatsiya Tahlili (Vertikal joylashuv)")

    with get_plot_figure(plot_revenue_by_year, "1. Yil bo'yicha O'rtacha Daromad") as fig:
        if fig:
            st.pyplot(fig, use_container_width=True)

    st.markdown("---")

    # 2. Budjet va Daromad
    with get_plot_figure(plot_budget_vs_revenue, "2. Budjet va Daromad O'rtasidagi Bog'liqlik") as fig:
        if fig:
            st.pyplot(fig, use_container_width=True)

    st.markdown("---")

    # 3. Runtime va Daromad
    with get_plot_figure(plot_runtime_vs_revnue, "3. Film Davomiyligi (Runtime) va Daromad O'rtasidagi Bog'liqlik") as fig:
        if fig:
            st.pyplot(fig, use_container_width=True)

    st.markdown("---")

    # 4. Janr bo'yicha O'rtacha Daromad
    with get_plot_figure(plot_genre_avg_revenue, "4. Janr bo'yicha O'rtacha Daromad") as fig:
        if fig:
            st.pyplot(fig, use_container_width=True)

    st.markdown("---")

    # 5. Janr bo'yicha O'rtacha Reyting
    with get_plot_figure(plot_genre_avg_rating, "5. Janr bo'yicha O'rtacha Reyting") as fig:
        if fig:
            st.pyplot(fig, use_container_width=True)
            
    st.markdown("---")



if __name__ == "__main__":
    main()