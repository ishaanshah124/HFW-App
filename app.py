import streamlit as st
import pandas as pd
import requests
from scoring import calc_all_players  

st.set_page_config(page_title="Fantasy Soccer Scoring", layout="wide")

st.title("⚽ HFW Soccer Scoring App")

link = st.text_input("Enter FBREF match link:")

if st.button("Calculate Scores"):
    if link:
        try:
            # Run your function
            results_df = calc_all_players(link)

            st.success("Scores calculated successfully ✅")

            # Show table
            st.dataframe(
                results_df.sort_values("score", ascending=False).reset_index(drop=True),
                use_container_width=True
            )

            # Extra: show top performers
            st.subheader("Top 5 Performers")
            top5 = results_df.sort_values("score", ascending=False).head(5)
            st.table(top5)

            # Download button
            csv = results_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Full Scores as CSV",
                data=csv,
                file_name="fantasy_scores.csv",
                mime="text/csv",
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a valid link.")


