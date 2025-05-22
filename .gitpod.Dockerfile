FROM gitpod/workspace-full

RUN pip install --upgrade jupyter ipywidgets

RUN pip install --no-cache-dir \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    scipy \
    scikit-learn \
    plotly \
    yellowbrick \
    kagglehub