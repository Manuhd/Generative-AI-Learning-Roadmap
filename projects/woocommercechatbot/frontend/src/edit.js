import { registerBlockType } from "@wordpress/blocks";
import Edit from "./index";
import "./style.css";

registerBlockType("woo/chatbot", {
  edit: Edit,
  save: () => {
    return <div id="woo-chatbot-frontend"></div>;
  },
});