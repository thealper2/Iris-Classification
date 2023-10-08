import React, { useState } from 'react';
import "./Iris.css";
import axios from "axios";

function Iris() {
    const [formData, setFormData] = useState({
        sepal_length: "",
        sepal_width: "",
        petal_length: "",
        petal_width: ""
    });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const resetFormData = () => {
        setFormData({
            sepal_length: "",
            sepal_width: "",
            petal_length: "",
            petal_width: ""
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            const response = await axios.post("http://localhost:8000/predict", formData)
            const data = response.data.data;
            const msg = `Prediction: ${data.result}`;
            alert(msg);
            resetFormData();
        } catch (error) {
            alert(`Error: ${error.messsage}`);
        }
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <h1>Iris Classification</h1>
                <div>
                    <label for="sepal_length">Sepal Length</label>
                    <input 
                     id="sepal_length"
                     name="sepal_length"
                     placeholder="Sepal Length"
                     required
                     autoFocus
                     pattern="[0-9]"
                     title="Sepal Length (0-5)"
                     type="number"
                     value={formData.sepal_length}
                     onChange={handleInputChange}
                    />
                </div>

                <div>
                    <label for="sepal_width">Sepal Width</label>
                    <input 
                     id="sepal_width"
                     name="sepal_width"
                     placeholder="Sepal Width"
                     required
                     autoFocus
                     pattern="[0-9]"
                     title="Sepal Width (0-5)"
                     type="number"
                     value={formData.sepal_width}
                     onChange={handleInputChange}
                    />
                </div>

                <div>
                    <label for="petal_length">Petal Length</label>
                    <input 
                     id="petal_length"
                     name="petal_length"
                     placeholder="Petal Length"
                     required
                     autoFocus
                     pattern="[0-9]"
                     title="Petal Length (0-5)"
                     type="number"
                     value={formData.petal_length}
                     onChange={handleInputChange}
                    />
                </div>

                <div>
                    <label for="petal_width">Petal Width</label>
                    <input 
                     id="petal_width"
                     name="petal_width"
                     placeholder="Petal Width"
                     required
                     autoFocus
                     pattern="[0-9]"
                     title="Petal Width (0-5)"
                     type="number"
                     value={formData.petal_width}
                     onChange={handleInputChange}
                    />
                </div>

                <div>
                    <button type="submit">Submit</button>
                </div>
            </form>
        </div>
    );
}

export default Iris;