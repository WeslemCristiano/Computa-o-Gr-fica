# 🖼️ Projeto de Filtros de Processamento de Imagens com Python (Pillow)

Este repositório contém um conjunto de scripts Python para aplicar diferentes filtros de **processamento de imagens**, 
organizados por categoria. Cada script utiliza a biblioteca [Pillow](https://python-pillow.org/) para aplicar um filtro 
específico sobre uma imagem de teste (`girafa.jpg`).

---

## 📌 Funcionalidades implementadas

| Categoria                         | Filtro Utilizado               |
|----------------------------------|--------------------------------|
| Realce e Ajuste de Intensidade   | Aumento de contraste e brilho |
| Redução de Ruído e Suavização    | `SMOOTH_MORE`                 |
| Detecção de Bordas               | `FIND_EDGES`                  |
| Detecção de Formas e Texturas    | `CONTOUR`                     |
| Transformações Geométricas       | Redimensionamento + Rotação   |
| Filtros Morfológicos             | `MinFilter` (simulando erosão) |

---

## 🧰 Requisitos

- Python 3.x
- Pillow

### 📦 Instalação das dependências

```bash
pip install Pillow
```

---

## ▶️ Como executar

1. Acesse a pasta da categoria desejada:
   ```bash
   cd filtros_imagem/1_realce_ajuste_intensidade
   ```

2. Execute o script:
   ```bash
   python script.py
   ```

3. A imagem processada será salva como `Teste1.jpg` (ou `transformada.jpg` no caso da transformação geométrica).

---

## 🦒 Imagem de Teste

A imagem utilizada para os testes foi uma foto de uma girafa, salva como `original.jpg` em cada pasta.

---

## 📷 Exemplo Visual (Antes x Depois)

| Original                        | Filtrada (Ajuste Intensidade)        |
|--------------------------------|--------------------------------------|
| ![original](1_realce_ajuste_intensidade/original.jpg) | ![filtrada](1_realce_ajuste_intensidade/filtrada.jpg) |

---

## ✍️ Autor

Desenvolvido por **[Weslem Cristiano]**

---
