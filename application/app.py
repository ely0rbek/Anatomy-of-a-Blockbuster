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
from blockbuster_analysis.actor_popularity_vs_avg_rating_movie import plot_actor_popularity_vs_avg_rating_movie

@contextmanager
# def get_plot_figure(plot_func, title):
#     try:
#         st.subheader(title)
#         plot_func()
#         fig = plt.gcf()
#         yield fig
#     except Exception as e:
#         st.error(f"'{title}' grafigini chizishda kutilmagan xatolik yuz berdi:")
#         st.exception(e)
#         yield None
#     finally:
#         if 'fig' in locals() and fig is not None:
#             plt.close(fig)

def get_plot_figure(plot_func, title):
    fig = None
    fig_width=6.4
    fig_height=4.8
    try:
        st.markdown(f"<h3 style='text-align: center;'>{title}</h3>", unsafe_allow_html=True)
        plt.close('all') 
        plt.figure(figsize=(fig_width, fig_height)) 
        plot_func()
        fig = plt.gcf()
        yield fig 
        
    except Exception as e:
        st.error(f"An error occurred while plotting '{title}':")
        st.exception(e)
        yield None
    finally:
        if fig is not None:
            plt.close(fig)

def main():
    st.set_page_config(page_title="Blockbuster Data Dashboard", layout="wide")
    title="Blockbuster Movies Data Analysis Dashboard"
    st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        with get_plot_figure(plot_revenue_by_year, "1. Average Income by Year") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)

    with col2:
        with get_plot_figure(plot_budget_vs_revenue, "2. Relationship Between Budget and Revenue") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)

    st.markdown("---")


    col3, col4 = st.columns(2)
    
    # 3-USTUN: Grafik 3
    with col3:
        with get_plot_figure(plot_runtime_vs_revnue, "3. Movie Runtime and Revenue Relationship") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)
                
    # 4-USTUN: Grafik 4
    with col4:
        with get_plot_figure(plot_genre_avg_revenue, "4. Average Revenue by Genre") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)
                
    st.markdown("---")
    
    # 5-grafikni markazda joylashtirish uchun yon tomondan bo'sh joy qoldiramiz
    # col5_left, col5_center, col5_right = st.columns([1, 2, 1])
    col5, col6 = st.columns(2)
    
    with col5:
        with get_plot_figure(plot_genre_avg_rating, "5. Average Rating by Genre") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)

    with col6:
        with get_plot_figure(plot_actor_popularity_vs_avg_rating_movie, "6. Regression: Actor Popularity → Average Ratinge") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)
                
    st.markdown("---")






    # with get_plot_figure(plot_revenue_by_year, "1. Yil bo'yicha O'rtacha Daromad") as fig:
    #     if fig:
    #         st.pyplot(fig, use_container_width=True)

    # st.markdown("---")

    # # 2. Budjet va Daromad
    # with get_plot_figure(plot_budget_vs_revenue, "2. Budjet va Daromad O'rtasidagi Bog'liqlik") as fig:
    #     if fig:
    #         st.pyplot(fig, use_container_width=True)

    # st.markdown("---")

    # # 3. Runtime va Daromad
    # with get_plot_figure(plot_runtime_vs_revnue, "3. Film Davomiyligi (Runtime) va Daromad O'rtasidagi Bog'liqlik") as fig:
    #     if fig:
    #         st.pyplot(fig, use_container_width=True)

    # st.markdown("---")

    # # 4. Janr bo'yicha O'rtacha Daromad
    # with get_plot_figure(plot_genre_avg_revenue, "4. Janr bo'yicha O'rtacha Daromad") as fig:
    #     if fig:
    #         st.pyplot(fig, use_container_width=True)

    # st.markdown("---")

    # # 5. Janr bo'yicha O'rtacha Reyting
    # with get_plot_figure(plot_genre_avg_rating, "5. Janr bo'yicha O'rtacha Reyting") as fig:
    #     if fig:
    #         st.pyplot(fig, use_container_width=True)
            
    # st.markdown("---")



if __name__ == "__main__":
    main()