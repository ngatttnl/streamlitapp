import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def app():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
    <a class="navbar-brand" href="https://thanhnga.herokuapp.com" target="_blank">Thanh Nga</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://www.youtube.com/channel/UCmcQhRJ6P9kF0cvtrEdDEoQ" target="_blank">YouTube</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://twitter.com/ngattt_tb" target="_blank">Twitter</a>
        </li>
      </ul>
    </div>
  </nav>
  """, unsafe_allow_html=True)
    st.title('Model')

    st.write('This is the `Model` page of the multi-page app.')

    st.write('The model performance of the Iris dataset is presented below.')

    # Load iris dataset
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    # Model building
    st.header('Model performance')
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    st.write('Accuracy:')
    st.write(score)