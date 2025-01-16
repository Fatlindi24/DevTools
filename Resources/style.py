# CSS specific to the Free API page
STYLE_CSS = """
    <style>
    .card {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #f8f9fa;
    padding: 15px;
    margin: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    text-align: center;
    height: auto;
    position: relative;
    overflow: hidden
    }

    .card img {
        width: 60px;
        height: 60px;
        margin-bottom: 10px;
    }

    .card-title {
        font-size: 16px;
        font-weight: bold;
        color: #333;
        margin: 5px 0;
    }

    .card-description {
        font-size: 14px;
        color: #555;
        margin-bottom: 20px;
    }

    .card-footer {
        width: 100%;
        text-align: center;
        margin-top: 10px; /* Add some spacing between footer and description */
    }

    .card-button {
        background-color: #FF4B4B;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }

    .card-button:hover {
        background-color: #ff7b7b;
    }
    </style>
"""