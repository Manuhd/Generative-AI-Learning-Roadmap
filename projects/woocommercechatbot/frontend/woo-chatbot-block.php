<?php
/**
 * Plugin Name: WooCommerce Chatbot Block
 * Description: Adds an AI-powered WooCommerce chatbot block.
 * Version: 1.0.1
 * Author: Manu HD
 */

function woo_chatbot_block_init() {
    wp_register_script(
        'woo-chatbot-block-editor',
        plugins_url('build/index.js', __FILE__),
        array('wp-blocks', 'wp-element', 'wp-editor', 'wp-components'),
        filemtime(plugin_dir_path(__FILE__) . 'build/index.js')
    );

    register_block_type(__DIR__, array(
        'editor_script' => 'woo-chatbot-block-editor',
        'render_callback' => 'woo_chatbot_block_render'
    ));
}
add_action('init', 'woo_chatbot_block_init');

function woo_chatbot_block_render() {
    // Enqueue frontend JS only on frontend
    wp_enqueue_script(
        'woo-chatbot-frontend',
        plugins_url('frontend.js', __FILE__),
        array(),
        filemtime(plugin_dir_path(__FILE__) . 'frontend.js'),
        true
    );

    // Add container for chatbot
    ob_start(); ?>
    <div id="woo-chatbot"></div>
    <?php
    return ob_get_clean();
}
