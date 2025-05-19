FROM gitpod/workspace-full

RUN pip install pandas numpy matplotlib kagglehub

RUN pip install --upgrade jupyter ipywidgets