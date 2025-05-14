// Color Picker component 
import { useState } from 'react';

export default function ColorPicker () {
    const [selectedColor, setSelectedColor] = useState({ hex: null, name: null });
    const [focusedIndex, setFocusedIndex] = useState(null);
    const [hoveredColor, setHoveredColor] = useState(null);
    const [toggled, setToggled] = useState(false);


    const colors = [
    { name: "Red", hex: "#FF0000" },
    { name: "Green", hex: "#00FF00" },
    { name: "Blue", hex: "#0000FF" },
    { name: "Yellow", hex: "#FFFF00" },
    { name: "Cyan", hex: "#00FFFF" },
    { name: "Magenta", hex: "#FF00FF" },
    ];

    function handleClick(color) {
        setSelectedColor(color);
    }

    function handleMouseEnter(colorHex) {
        setHoveredColor(colorHex);
    }

    function handleMouseLeave() {
        setHoveredColor(null);
    }

    function handleFocus(index) {
        setFocusedIndex(index);
    }

    function handleBlur() {
        setFocusedIndex(null);
    }

   function handleKeyDown(e, index) {
        if (e.key === "Enter" || e.key === " ") {
            const newToggledState = !toggled;
            setToggled(newToggledState);
            e.target.style.backgroundColor = newToggledState ? "#000" : colors[index].hex;
        }
    }

    return (
        <div className="color-picker">
            <h1>Color Picker</h1>
            <div className="color-list">
                {colors.map((color, index) => (
                <div
                    key={index}
                    className={`color-item ${focusedIndex === index ? 'focused' : ''}`}
                    style={{ backgroundColor: color.hex }}
                    onClick={() => handleClick(color)}
                    onMouseEnter={() => handleMouseEnter(color.hex)}
                    onMouseLeave={handleMouseLeave}
                    onFocus={() => handleFocus(index)}
                    onBlur={handleBlur}
                    onKeyDown={(e) => handleKeyDown(e, index)}
                    tabIndex={0}
                >
                    {selectedColor.hex === color.hex && (
                    <span className="color-code">{selectedColor.name || color.hex}</span>
                    )}

                    {hoveredColor === color.hex && (
                        <span className="color-code">{color.name || color.hex}</span>
                    )}
                </div>
                ))}
            </div>
        </div>
    );
}
