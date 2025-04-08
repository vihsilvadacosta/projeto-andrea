
# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Coleta de Logs - Simulação do arquivo de log
data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'session_duration': [10, 20, 30, 50, 15, 100, 5, 80, 25, 300],
    'pages_visited': [5, 6, 7, 10, 8, 50, 3, 20, 7, 200],
    'purchase_made': [0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    'timestamp': pd.date_range('2023-03-01', periods=10, freq='D')
}
df_logs = pd.DataFrame(data)
df_logs.to_csv('user_logs.csv', index=False)

# 2. Ingestão - Carregar o arquivo de log
df = pd.read_csv('user_logs.csv')
print("Logs carregados:")
print(df.head())

# 3. Pré-processamento
df['session_duration'] = (df['session_duration'] - df['session_duration'].min()) / (df['session_duration'].max() - df['session_duration'].min())
df['pages_visited'] = (df['pages_visited'] - df['pages_visited'].min()) / (df['pages_visited'].max() - df['pages_visited'].min())

# 4. Detecção de Anomalias
model = IsolationForest(contamination=0.2)
df['anomaly_score'] = model.fit_predict(df[['session_duration', 'pages_visited']])

# 5. Classificação
df['classification'] = df['anomaly_score'].apply(lambda x: 'Normal' if x == 1 else 'Suspeito')

# 6. Alertas
alerts = df[df['classification'] == 'Suspeito']
print("\nAlertas gerados para acessos críticos:")
print(alerts[['user_id', 'classification', 'session_duration', 'pages_visited']])
alerts.to_csv('alertas_criticos.csv', index=False)

# 7. Visualização
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='session_duration', y='pages_visited', hue='classification', palette='viridis')
plt.title('Análise de Logs de Usuários - Duração da Sessão vs Páginas Visitadas')
plt.xlabel('Duração da Sessão (Normalizada)')
plt.ylabel('Páginas Visitadas (Normalizada)')
plt.legend(title='Classificação')
plt.show()

# Exibindo a tabela final dos logs processados
print("\nLogs após processamento:")
print(df[['user_id', 'session_duration', 'pages_visited', 'classification']])
