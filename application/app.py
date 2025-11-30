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
from blockbuster_analysis.runtime_vs_revenue import plot_runtime_vs_revenue
from blockbuster_analysis.actor_popularity_vs_avg_rating_movie import plot_actor_popularity_vs_avg_rating_movie
from blockbuster_analysis.movie_count_by_year import plot_movie_count_by_year
from blockbuster_analysis.avg_rating_by_year import plot_avg_rating_by_year

@contextmanager
def get_plot_figure(plot_func, title):
    fig = None
    fig_width=8
    fig_height=5
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
        with get_plot_figure(plot_movie_count_by_year,"Number of Movies Released per Year (1950–2022)") as fig:
            if fig:
                st.pyplot(fig,use_container_width=True)

    with col2:
        with get_plot_figure(plot_avg_rating_by_year, "Average Rating by Year (1950–2022)") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)


    st.markdown("---")


    col2_9, col3,col3_1=st.columns([1,2,1])
    with col3:
        with get_plot_figure(plot_revenue_by_year, "Average Revenue by Year") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)


    col4,col5 = st.columns(2)
    
    with col4:
        with get_plot_figure(plot_genre_avg_revenue, "Average Revenue by Genre") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)
    
    with col5:
        with get_plot_figure(plot_genre_avg_rating, "Average Rating by Genre") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)
    
    st.markdown("---")


    col6, col7 = st.columns(2)

    with col6:
        with get_plot_figure(plot_budget_vs_revenue, "Relationship Between Budget and Revenue") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)

    with col7:
        with get_plot_figure(plot_runtime_vs_revenue, "Movie Runtime and Revenue Relationship") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)


    col7_9,col8,col8_1 = st.columns([1,2,1])

    with col8:
        with get_plot_figure(plot_actor_popularity_vs_avg_rating_movie, "Regression: Actor Popularity → Average Ratinge") as fig:
            if fig:
                st.pyplot(fig, use_container_width=True)
                
    st.markdown("---")




if __name__ == "__main__":
    main()