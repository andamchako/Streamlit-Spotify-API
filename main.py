"""

"""
# Dependencies
import streamlit as st
from functions import *
from streamlit_tags import st_tags
import numpy as np


# st.set_page_config(layout="wide")

# App declaration
def main():
    # Header contents
    st.write('# Spotify Song Recommendations')

    # Input up to 10 artists
    st.info('Input up-to 10 artists. Spelling matters.', icon="ℹ️")
    artists = st_tags(
        label='### Enter Artists:',
        text='Press enter to add more',
        maxtags=10,
        key='1')

    # Perform top-10 song recommendation generation
    if st.button("Recommend"):
        try:

            # get the artist_id for each artist from input list
            artist_list = [get_artist(artist)['id'] for artist in artists]

            with st.spinner('Crunching the numbers...'):

                # make recommendations
                top_recommendations = show_recommendations_for_artist(artist_list)

            st.subheader("Songs you might like:\n")

            st.write('')

            # reshape output list into a 5x4 array
            rec_array = np.reshape(top_recommendations, (5, 4))

            tab1, tab2, tab3, tab4, tab5 = st.tabs(["Page 1", "Page 2", "Page 3", "Page 4", "Page 5"])

            with tab1:
                col1, col2 = st.columns(2, gap='small')

                with col1:
                    for track in rec_array[0][:2]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

                with col2:
                    for track in rec_array[0][2:]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

            with tab2:
                col1, col2 = st.columns(2, gap='small')

                with col1:
                    for track in rec_array[1][:2]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

                with col2:
                    for track in rec_array[1][2:]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

            with tab3:
                col1, col2 = st.columns(2, gap='small')

                with col1:
                    for track in rec_array[2][:2]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

                with col2:
                    for track in rec_array[2][2:]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

            with tab4:
                col1, col2 = st.columns(2, gap='small')

                with col1:
                    for track in rec_array[3][:2]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

                with col2:
                    for track in rec_array[3][2:]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

            with tab5:
                col1, col2 = st.columns(2, gap='small')

                with col1:
                    for track in rec_array[4][:2]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')

                with col2:
                    for track in rec_array[4][2:]:
                        st.markdown(
                            f"[![Foo]({track['album']['images'][1]['url']})]({track['external_urls']['spotify']})")
                        st.subheader(track['artists'][0]['name'])
                        st.markdown(track['name'])
                        st.write('-------------------------------')
        except Exception:
            raise


if __name__ == '__main__':
    main()
